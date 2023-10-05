<?php

use Symfony\Component\Routing\Route;
use Symfony\Component\Routing\RouteCollection;

$routes = new RouteCollection();

$routes->add("route_index",
    new Route('/', ['controller' => 'UserController::index'])
);

// ajoute le prefix à tous les chemins de la collection users
$routes->addPrefix("/users");


return $routes;