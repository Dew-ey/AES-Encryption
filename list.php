<?php
header('Access-Control-Allow-Origin: *');
$dir = "/var/www/html/uploads/";
$files = scandir($dir);
echo json_encode($files);
?>
