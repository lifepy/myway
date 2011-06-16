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
				_uploadphoto.showCities(data);
			},
		});
	}
	
	this.showCities = function(data) {
		var option;
		data.forEach(function(city){
			option = "<option value='" + city + "'>" + city + "</option>";
			$("#city").append(option);
		})
	}
}