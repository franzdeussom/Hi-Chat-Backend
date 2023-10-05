<?php

require_once __DIR__ . "/../autoload.php";

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

class UserController extends BaseController
{
    const COLUMNS = array("name", "surname", "email", "age", "gender", "phone", "birthday", "password");

    /**
     * @param Request $request
     * @param array $args
     * @return Response
     */
    public function index(Request $request, array $args): Response
    {
        if ($request->isMethod("GET")) {
            return $this->getAllUsers($request, $args);
        } elseif ($request->isMethod("POST")) {
            return $this->createUser($request, $args);
        }
        return new Response("", Response::HTTP_METHOD_NOT_ALLOWED);
    }

    /**
     * @param Request $request
     * @param array $args
     * @return Response
     */
    public function getAllUsers(Request $request, array $args): Response
    {
        $users = $this->db->fetch(
            "SELECT Users.id, name, surname, email, age, gender, phone, birthday, password, country, city, profile, created_at, account_type FROM Users");

        return new JsonResponse($users ?? []);
    }

    /**
     * @param Request $request
     * @param array $args
     * @return Response
     */
    public function createUser(Request $request, array $args): Response
    {
        $valid = $this->allKeysExists(self::COLUMNS, $request->request->all());
        print_r($request->request->all());
        if (!$valid[0]) {
            return new Response("missing required field $valid[1]\n required fields are " . json_encode(self::COLUMNS), Response::HTTP_BAD_REQUEST);
        }

        $profile = "";
        if ($request->request->get("profile") !== null) {
            $profile = Avatar::handleUpload($request->request->get("profile"));
        }

        $password = password_hash($request->request->get("password"));

        $this->db->execute(
            "INSERT INTO Users(name, surname, email, age, gender, phone, birthday, password, country, city) 
            VALUE (
                   :name, 
                   :surname, 
                   :email, 
                   :age, 
                   :gender, 
                   :phone, 
                   :birthday, 
                   :password, 
                   :country, 
                   :city
            )",
            array());// TODO

        return new Response("on");
    }

}

