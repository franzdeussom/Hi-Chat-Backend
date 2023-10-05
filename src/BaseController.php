<?php

require_once __DIR__ . '/autoload.php';

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

abstract class BaseController
{
    /**
     * @var DatabaseHelper|null
     */
    protected ?DatabaseHelper $db = null;

    public function __construct()
    {
        DatabaseHelper::configure("localhost", "HiChat", "root", "");
        $this->db = DatabaseHelper::getInstance();
        $this->db->setFetchMode(PDO::FETCH_ASSOC);
    }

    /**
     * verifies if all keys are present in a variable
     * @param array $keys
     * @param mixed $data
     * @return array
     */
    public function allKeysExists(array $keys, mixed $data): array
    {

        foreach ($keys as $key) {
            if (!isset($data[$key])) return [false, $key];
        }
        return [true];
    }

    /**
     * verifies if request has raw data
     * @param Request $request
     * @return bool
     */
    public function hasRawData(Request $request): bool
    {
        return !empty($request->getContent());
    }

    /**
     * @param Request $request
     * @param array $args
     * @return Response
     */
    public abstract function index(Request $request, array $args): Response;
}