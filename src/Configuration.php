<?php
require_once __DIR__ . '/autoload.php';
require_once __DIR__ . '/utils/functions.php';

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Exception\ResourceNotFoundException;
use Symfony\Component\Routing\Matcher\UrlMatcher;
use Symfony\Component\Routing\RequestContext;
use Symfony\Component\Routing\RouteCollection;


class Configuration
{
    public static array $MIDDLEWARES = array();
    public static array $INSTALLED_MODULES = array();
    private Request $request;

    private RouteCollection $routeCollection;

    public function __construct()
    {
        $this->routeCollection = new RouteCollection();
        $this->request = Request::createFromGlobals();

        $this->applyMiddleware();

        $this->addModulesRoutes();
    }

    private function applyMiddleware(): void
    {
        foreach (self::$MIDDLEWARES as $MIDDLEWARE) {
            call_user_func_array(explode("::", $MIDDLEWARE), [$this->request]);
        }
    }

    private function addModulesRoutes(): void
    {
        foreach (self::$INSTALLED_MODULES as $MODULE) {
            if (is_dir($MODULE)) {
                $route = $MODULE . DIRECTORY_SEPARATOR . "routes.php";
                if (file_exists($route)) {
                    $routes = require_once $route;
                    if (is_a($routes, RouteCollection::class))
                        $routes = normalize_route_collection($routes);
                    $this->routeCollection->addCollection($routes);
                }
            }
        }
    }

    public function exec(): void
    {
        $requestContext = new RequestContext();
        $requestContext->fromRequest($this->request);
        $matcher = new UrlMatcher($this->routeCollection, $requestContext);

        try {
            $parameters = $matcher->match($this->request->getPathInfo());
            $action = explode('::', $parameters['controller']);

            // Traitez la route et appelez le contrôleur approprié
            if (count($action) == 1) {
                $response = call_user_func_array([new $action[0](), 'index'], [$this->request, $parameters]);
            } else {
                $response = call_user_func_array([new $action[0](), $action[1]], [$this->request, $parameters]);

            }
            if ($response) {
                $response->send();
            }
        } catch (ResourceNotFoundException $e) {
            // Gérez le cas où la route n'a pas été trouvée
            http_response_code(404);
            echo "Page " . $this->request->getPathInfo() . " non trouvée.";
        } catch (Exception $e) {
            http_response_code(500);
            echo $e;
        }
    }

    private function showAllRoutes(): void
    {
        foreach ($this->routeCollection->all() as $route) {
            echo $route->getPath();
        }
    }
}