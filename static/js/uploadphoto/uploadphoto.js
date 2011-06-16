// myway js definition
// version 1.0
// author victor.you

_uploadphoto = new function() {
	this.selProvince = function(province) {
		$.ajax({
			type: "GET",
			url: "/console/getCitiesByProvince",
			dataType: "json",
			data: {
				province:province
			},
			success: function(data) {
				_uploadphoto.showCities(data.cities);
			}
		});
	}
	
	this.showCities = function(cities) {
		$("#city").empty();
		for (var i = 0; i < cities.length; i++) {
			var city = cities[i];
			var option = "<option value='" + city + "'>" + city + "</option>";
			$("#city").append(option);
		}
	}
}