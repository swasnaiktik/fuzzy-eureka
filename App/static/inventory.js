changeQuantity = (item, action) => {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function (){
        if (this.readyState === 4 && this.status === 200){
            var itemTag = document.getElementById(item);
            if(request.response === "Success"){
                if(action === "increase"){
                    console.log(itemTag.innerHTML)
                    itemTag.innerHTML = Number(itemTag.innerHTML) + 1
                }else{
                    itemTag.innerHTML = Math.max(Number(itemTag.innerHTML) - 1, 0)
                }
            }
        }
    }
    request.open("GET", item + "/" + action)
    request.send()
}