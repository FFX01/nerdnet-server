from django.shortcuts import render
from django.views.generic import View


class ImageList(View):

    def get(self, request):
        return render(
            request=request,
            template_name='media/views/image-list.html',
            context={}
        )


class ImageDetail(View):

    def get(self, request, pk):
        return render(
            request=request,
            template_name='media/views/image-detail.html',
            context={
                'pk': pk
            }
        )


class ImageCreate(View):

    def get(self, request):
        return render(
            request=request,
            template_name='media/views/image-create.html',
            context={}
        )
