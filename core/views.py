from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

def BootstrapFilterView(request):
    template_name = "core/bootstrap_form.html"
    context = {

    }
    return render(request, template_name, context)


