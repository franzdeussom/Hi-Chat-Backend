<?php
header('Access-Control-Allow-Origin: http://localhost:8100');
header('Access-Control-Allow-Credentials: true');
header('Access-Control-Allow-Methods: *');
header('Access-Control-Allow-Headers: Authorization, Content-Type, Deplth, User-Agent, X-File-Size, X-Requested-With, If-Modified-Since, X-File-Name, Cache-Control');

require_once '../vendor/autoload.php';
require_once './autoload.php';

$routes = require_once __DIR__ . '/settings.php';

$configuration = new Configuration();


$configuration->exec();

