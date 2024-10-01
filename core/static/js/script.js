// Função para lidar com a abertura do pop-up
function openPopup(titulo, artista) {
    document.getElementById("popup").style.display = "block";
    document.getElementById("musicName").innerText = titulo;
    document.getElementById("musicInfo").innerText = artista;
    document.getElementById("menu-container").style.display = "none";
}

// Função para lidar com o fechamento do pop-up
function closePopup() {
    document.getElementById("popup").style.display = "none";
    document.getElementById("menu-container").style.display = "block";
}

// Adiciona event listeners aos botões
/* document.getElementById("openPopup").addEventListener("click", openPopup);
document.getElementById("closePopup").addEventListener("click", closePopup); */