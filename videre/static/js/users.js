

function criaLinha(usuario) {
    const linha = document.createElement("tr");
    const tdId = document.createElement("td");
    const tdNome = document.createElement("td");
    tdId.textContent = usuario.id;
    tdNome.textContent = usuario.nome;
    linha.appendChild(tdId);
    linha.appendChild(tdNome);
    return linha;
}

function getUsuarios() {
    fetch("http://127.0.0.1:5000/usuarios/")
        .then(response => response.json())
        .then(usuarios => {
            const tabela = document.getElementById("tabela");
            usuarios.forEach(usuario => {
                const linha = criaLinha(usuario);
                tabela.appendChild(linha);
            });
        })
        .catch(error => console.log(error));
}

function exibirUsuarios() {
    const modal = document.getElementById("ver_users");
    modal.showModal();
    getUsuarios();
    const fecharButton = document.createElement("button");
    fecharButton.textContent = "Fechar";
    fecharButton.setAttribute("id", "fechar_button")
    fecharButton.onclick = function () {
        modal.close();
    };
    modal.appendChild(fecharButton);
}

function postarUsuario() {
    const url = "http://127.0.0.1:5000/usuarios/";
    const nome = document.getElementById("nome").value;
    const senha = document.getElementById("senha").value;
    const body = {
        "nome": nome,
        "senha": senha
    };
    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(body)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));
}


