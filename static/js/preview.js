document.getElementById('image-preview').style.display = 'none';
document.getElementById('upload-icon').style.display = 'block';

document.getElementById('id_image').addEventListener('change', function () {
    const file = this.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        document.getElementById('image-preview').style.display = 'block';
        document.getElementById('upload-icon').style.display = 'none';
        document.getElementById('image-preview').setAttribute('src', e.target.result);
    }

    reader.readAsDataURL(file);
});