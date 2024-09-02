function toggleForm() {
    var formContainer = document.getElementById("form-container");
    if (formContainer.style.display === "none" || formContainer.style.display === "") {
        formContainer.style.display = "block";
    } else {
        formContainer.style.display = "none";
    }
}

function openModal(idFuncionario, cpfFuncionario, nomeFuncionario) {
    document.getElementById("editIdFuncionario").value = idFuncionario;
    document.getElementById("editCpfFuncionario").value = cpfFuncionario;
    document.getElementById("editNomeFuncionario").value = nomeFuncionario;

    var form = document.getElementById("editForm");
    form.action = "{{ url_for('editar_funcionario', idFuncionario=0) }}" + idFuncionario;

    var modal = document.getElementById("editModal");
    modal.style.display = "block";
}


function closeModal() {
    var modal = document.getElementById("editModal");
    modal.style.display = "none";
}

window.onclick = function(event) {
    var modal = document.getElementById("editModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}