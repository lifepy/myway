// myway js definition
// version 1.0
// author victor.you

_updshr = new function() {
	this.addFileField = function() {
		var fileCount = $("#shareForm :file").length;
		var newFileField = '<p><label for="id_file' + fileCount;
		newFileField += '">File:</label> <input type="file" name="file';
		newFileField += fileCount + '" id="id_file' + fileCount + '"></p>';
		$('#addFileFieldLink').before(newFileField);
	}
}