<?php
header('Access-Control-Allow-Origin: *');
$maxFileSize = 5000000;
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  echo "POST Detected";
  $target_dir = "/var/www/html/uploads/";
  $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
  echo $target_file;
  if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
    echo "The file ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " has been uploaded.";
  } 
  else {
    echo "Sorry, there was an error uploading your file.";
  }
} 
else {
  echo "Invalid request method.";
}
?>
