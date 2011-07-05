// myway js definition
// version 1.0
// author victor.you

_uploadphoto = new function() {
	this.selProvince = function(province_id) {
		$.ajax({
			type: "GET",
			url: "/json/subareas/in/"+province_id+'/',
			dataType: "json",
			//data: {
		    //		province:province_id
			//},
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
			url: "/place/restraunts/in/" + area_id + '/json/',
			dataType: "json",
			data: {
				area_id:area_id
			},
			success: function(spotList) {
				// spot input box auto complete using autocomplete plugin
				$("#place").flushCache();
				$("#place").autocomplete(spotList,{minChars: 0});
			}
		});
	}
	
	this.showInfo = function(spot_name) {
		$.ajax({
			type: "GET",
			url: "/place/photos/" + spot_name + '/json/',
			dataType: "json",
			data: {
				spot_name:spot_name
			},
			success: function(photolist) {
				console.debug(photolist);
				_uploadphoto.showPhotos(photolist);
			}
		});
	}
	
	this.showPhotos = function(photos) {
		$("#photos").empty();
		for (var i = 0; i < photos.length; i++) {
			var photoId = photos[i];
			var photoDiv = "<div><img src='/gridfs/photo/" + photoId + "'/></div>";
			$("#photos").append(photoDiv);
		}
	}
	
	this.init = function() {
		$("#province")[0].options[9].selected = true;
		this.selProvince($("#province").val());
	}
}

$(function() {_uploadphoto.init()});
