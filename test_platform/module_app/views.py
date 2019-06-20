from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from module_app.models import Module
from module_app.forms import ModuleForm
# Create your views here.


@login_required
def module_manage(request):
    """
    模块管理
    :param request:
    :return:
    """
    if request.method == "GET":
        module_all = Module.objects.all()
        return render(request, "module.html", {"modules": module_all, "type": "list"})


@ login_required
def add_module(request):
    """
    添加模块
    """
    if request.method == "GET":
        module_form = ModuleForm()
        return render(request, "module.html", {"form": module_form, "type": "add"})

    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]
            Module.objects.create(project=project, name=name, describe=describe)

            return HttpResponseRedirect("/module/")  # 重定向到 module.html 页面


def edit_module(request, mid):
    """
    编辑模块
    :param request:
    :param mid:
    :return:
    """
    if request.method == "GET":
        module = Module.objects.get(id=mid)
        module_form = ModuleForm(instance=module)
        module_dict = {
             "form": module_form,
             "id": module.id,
             "type": "edit"
         }
        return render(request, "module.html", module_dict)

    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]

            m = Module.objects.get(id=mid)
            m.name = name
            m.desctibe = describe
            m.project = project
            m.save()
            return HttpResponseRedirect('/module/')  # 重定向到 module.html 页面


def delete_module(request, mid):
    """
    删除模块
    :param request:
    :param mid:
    :return:
    """
    if request.method == "GET":
        try:
            module = Module.objects.get(id=mid)
        except Module.DoesNotExist:
            return HttpResponseRedirect("/module/")
        else:
            module.delete()
        return HttpResponseRedirect("/module/")
    else:
        return HttpResponseRedirect("/module/")


def get_module_list(request):
    """
    接口: 根据项目id, 返回对应的模块列表
    :param request:
    :return:
    """
    if request.method == "POST":
        pid = request.POST.get("pid", "")
        if pid == "":
            return JsonResponse({"status": 10102, "message": "项目id不能为空"})

        modules = Module.objects.filter(project=pid)
        module_list = []
        for mod in modules:
            module_dict = {
                "id": mod.id,
                "name": mod.name
            }
            module_list.append(module_dict)
        return JsonResponse({"status": 10200, "message": "请求成功", "data": module_list})
    else:
        return JsonResponse({"status": 10101, "message": "请求方法错误"})