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
		this.selCity($("#city").val());
	}
	
	this.selCity = function(city_id) {
		$.ajax({
			type: "GET",
			url: "/json/subareas/in/" + city_id + '/',
			dataType: "json",
			data: {
				city:city_id
			},
			success: function(zones) {
				_uploadphoto.showZones(zones);
			}
		});
	}
	
	this.showZones = function(zones) {
		$("#zone").empty();
		for (var i = 0; i < zones.length; i++) {
			var zone = zones[i];
			var option = "<option value='" + zone['id'] + "'>" + zone['name'] + "</option>";
			$("#zone").append(option);
		}
		this.selZone($("#zone").val());
	}
	
	this.selZone = function(area_id) {
		$.ajax({
			type: "GET",
			url: "/json/getspots/" + area_id + '/',
			dataType: "json",
			data: {
				area_id:area_id
			},
			success: function(spotList) {
				// spot input box auto complete using autocomplete plugin
				$("#spot").flushCache();
				$("#spot").autocomplete(spotList,{minChars: 0});
			}
		});
	}
	
	this.init = function() {
		$("#province")[0].options[10].selected = true;
		this.selProvince($("#province").val());
	}
}

$(function() {_uploadphoto.init()});
