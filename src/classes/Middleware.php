<?php

use Symfony\Component\HttpFoundation\Request;

class Middleware
{
    /**
     * @param Request $request
     * @return void
     */
    public static function transformJsonContent(Request $request): void
    {
        if ($request->headers->contains("Content-Type", "application/json") and $request->getContent()) {
            try {
                $data = json_decode($request->getContent(), true);
                $request->request->add($data);
            } catch (Exception $e) {
            }
        }
    }

    public static function transformBase64ToTempFile(Request $request)
    {
        // TODO
    }
}