const dialog = document.getElementById("confirm-dialog");
const message = document.getElementById("confirm-message");

const cancelBtn = document.getElementById("cancel-btn");
const confirmBtn = document.getElementById("confirm-btn");

async function showDeletionConfirm(dishId, dishName) {
    message.innerHTML = `¿Estás seguro de eliminar el platillo <b>${dishName}</b>?`;
    dialog.showModal();

    await new Promise(resolve => {
        dialog.addEventListener('close', resolve, { once: true });
    });

    if(dialog.returnValue === "confirm"){
        window.location.href=`/${dishId}/delete/`;
    }
}

cancelBtn.addEventListener("click", ()=>{
    dialog.close("cancel");
});

confirmBtn.addEventListener("click", ()=>{
    dialog.close("confirm");
});