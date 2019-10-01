document.addEventListener("DOMContentLoaded", loadDB, false);

function loadDB(e) {
    var params = '';
    params = window.location.search;
    param = params.split('=');
    if(param[0]=='?style') {
        fetch('http://localhost:8080/discs/style/'+param[1]).then(response => response.json()).then(data => displayShop(data));
    }
    else if(param[0]=='?id') {
        fetch('http://localhost:8080/discs/'+param[1]).then(response => response.json()).then(data => displayDeets(data));
    }
    else{
        fetch('http://localhost:8080/discs/').then(response => response.json()).then(data => displayShop(data));
    }
}

function displayShop(data) {
    let DOMstring = '';
    for(i=0; i < data.length; i++) {
        DOMstring += '<div class="product"> <a href="details.html?id='+(data[i].id)+'"><img class="product__pic" src="images/'+data[i].img+'" alt="desc"></a> <h3 class="product__name">'+data[i].model+'</h3> <p>'+data[i].descr+'</p> <p class="price">'+data[i].price+'</p> </div>';
    }
    document.querySelector(".grid-shop").innerHTML = DOMstring; 
}

function displayDeets(data) {
    document.querySelector(".detail").innerHTML = '<img class="detail__pic" src="images/'+data.img+'" alt="desc"> <img class="detail__pic" src="images/'+data.img2+'" alt="desc">';
    document.querySelector(".dethead").innerHTML = data.model;
    document.querySelector(".insert").innerHTML = '<p>'+data.descr+'</p> <p class="price">$'+data.price+'</p>';
}
