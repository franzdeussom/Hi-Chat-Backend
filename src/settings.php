<?php


Configuration::$MIDDLEWARES = array(
    "Middleware::transformJsonContent", // transformer les données json en paramètres POST
);

Configuration::$INSTALLED_MODULES = array(
    __DIR__ . "/Users"
);