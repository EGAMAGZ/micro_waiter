const imagePreview = document.getElementById('image-preview');
const uploadIcon = document.getElementById('upload-icon');

if (imagePreview.src && imagePreview.src !== window.location.href) {
    imagePreview.style.display = 'block';
    uploadIcon.style.display = 'none';
} else {
    imagePreview.style.display = 'none';
    uploadIcon.style.display = 'block';
}

document.getElementById('id_image').addEventListener('change', function () {
    const file = this.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        imagePreview.style.display = 'block';
        uploadIcon.style.display = 'none';
        imagePreview.src = e.target.result;
    }

    if (file) {
        reader.readAsDataURL(file);
    }
});