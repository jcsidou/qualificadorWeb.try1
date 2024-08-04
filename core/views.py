from django.shortcuts import render
from .forms import UploadFileForm
from .utils import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return render(request, 'core/success.html')
    else:
        form = UploadFileForm()
    return render(request, 'core/upload.html', {'form': form})
