function getBathValue() {
    var bathrooms = document.getElementsByName("uiBATH");
    for (var i = 0; i < bathrooms.length; i++) {
        if (bathrooms[i].checked) {
            return parseInt(bathrooms[i].value);
        }
    }
    return -1;
}

function getBedValue() {
    var beds = document.getElementsByName("uiBED");
    for (var i = 0; i < beds.length; i++) {
        if (beds[i].checked) {
            return parseInt(beds[i].value);
        }
    }
    return -1;
}

function onClickedEstimatePrice() {
    var sqft = document.getElementById("uiSqft");
    var bed = getBedValue();
    var bath = getBathValue();
    var sublocality = document.getElementById("uiSublocalities");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_home_price";

    $.post(url, {
        sqft: parseFloat(sqft.value),
        beds: bed,
        bath: bath,
        sublocality: sublocality.value
    }, function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " $</h2>";
        console.log(status);
    });
}

function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_sublocality_names";
    $.get(url, function(data, status) {
        console.log("got response for get_sublocality_names request");
        if (data) {
            var sublocalities = data.sublocalities;
            var uiSublocalities = document.getElementById("uiSublocalities");
            $('#uiSublocalities').empty();
            for (var i in sublocalities) {
                var opt = new Option(sublocalities[i]);
                $('#uiSublocalities').append(opt);
            }
            console.log(status);
        }
    });
}

window.onload = onPageLoad;
