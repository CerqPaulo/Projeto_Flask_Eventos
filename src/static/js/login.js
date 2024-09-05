document.getElementById('submit-button').addEventListener('click', function() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username && password) {
        alert(`Usuário: ${username}\nSenha: ${password}`);
        // Aqui você pode adicionar a lógica para enviar os dados para o servidor ou realizar outra ação
    } else {
        alert('Por favor, preencha todos os campos.');
    }
});
