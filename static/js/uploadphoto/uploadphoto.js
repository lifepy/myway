// myway js definition
// version 1.0
// author victor.you

_uploadphoto = new function() {
	this.selProvince = function(province_id) {
		$.ajax({
			type: "GET",
			url: "/json/subareas/in/"+province_id+'/',
			dataType: "json",
			data: {
				province:province_id
			},
			success: function(cities) {
				_uploadphoto.showCities(cities);
			}
		});
	}
	
	this.showCities = function(cities) {
		$("#city").empty();
		for (var i = 0; i < cities.length; i++) {
			var city = cities[i];
			var option = "<option value='" + city['id'] + "'>" + city['name'] + "</option>";
			$("#city").append(option);
		}
	}
}
