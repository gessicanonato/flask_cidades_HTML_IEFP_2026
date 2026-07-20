function confirmaEliminar(cidade,id){
    let mensagem = "Tem a certeza que pretende eliminar a cidade " + cidade + "?";
    let href= "eliminar.php?cidade_id=" + id;
    
    // criar mensagem
    document.getElementById("textoAviso_id").innerText = mensagem;
    // criar url para link do botão "Ok"
    document.getElementById("aviso_ok_id").href = href;
    // tornar a janela visível
    document.getElementById("janelaAvisos_id").style.display = "block";
}

function removerJanelaAviso(){ 
    document.getElementById("janelaAvisos_id").style.display = "none";
}
function removerJanelaAlerta(){ 
    document.getElementById("janelaAlertas_id").style.display = "none";
}