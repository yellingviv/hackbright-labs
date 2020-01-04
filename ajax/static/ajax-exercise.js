"use strict";

// PART 1: SHOW A FORTUNE

function showFortune(evt) {
  $.get('/fortune', (response) => {
    $('#fortune-text').html(response);
  });
}

$('#get-fortune-button').on('click', showFortune);





// PART 2: SHOW WEATHER

function showWeather(evt) {
    evt.preventDefault();

    let url = "/weather.json";
    let formData = {"zipcode": $("#zipcode-field").val()};

    $.get(url, formData, (res) => {
      $('#weather-info').text(res.forecast);
    });
}

$("#weather-form").on('submit', showWeather);




// PART 3: ORDER MELONS

function orderMelons(evt) {
    evt.preventDefault();

    let url = "/order-melons.json";
    let formData = {"melon_type": $("#melon-type-field").val(),
                    "qty": $("#qty-field").val()};

    $.post(url, formData, (res) => {
      $("#order-status").text(res.msg);
      if (res.code === "ERROR") {
        $("#order-status").addClass("order-error");
      }
    });
}

$("#order-form").on('submit', orderMelons);


