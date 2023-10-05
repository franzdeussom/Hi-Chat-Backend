<?php

use Symfony\Component\Routing\RouteCollection;


/**
 * solve problems with trailing slash
 * @param RouteCollection $routes
 * @return RouteCollection
 */
function normalize_route_collection(RouteCollection $routes): RouteCollection
{
    foreach ($routes->all() as $route) {
        $_route = rtrim($route->getPath(), "/");
        $route->setPath("$_route{slash}");
        $route->setDefault("slash", "");
        $route->setRequirement("slash", "/?");
    }
    return $routes;
}