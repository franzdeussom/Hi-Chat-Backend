<?php
    require_once 'vendor/autoload.php';
    use Firebase\JWT\JWT;
    use Firebase\JWT\Key;
    
    $algo = 'HS256';
    $myKey = 'HI-Chat-FranzDeussom2023';

    function generateToken($userID){
        global $algo;
        global $myKey;

        $payload = [
            'sub' => strval($userID),
            'name' => 'Franz Deussom2023',
            'iat' => time(),
            'exp' => time() + (60 * 60), // Expires in 1 hour
        ];

        $token = JWT::encode($payload, $myKey, $algo);
        return $token;
    }
    
    function verifiedToken($authorization){
        global $algo;
        global $myKey;

        if(is_null($authorization)){
            $authorization = 'FranzDeussom';
        }
        
        try{
            $decoded = JWT::decode($authorization, new Key($myKey, $algo));
            return true;
            
        }catch(Exception $e){
            http_response_code(403);
            return false;
        }
    }


    
    /*class TokenManager{
        private $tokensList;
        private static $instance = null;
        private $secretKey = 'HiChat-Franz2003';
        private $algo  = 'aes-256-cbc';

        private function __construct() {
            $this->tokensList = [];
        }

        public static function getInstance(){
                if(!self::$instance || self::$instance == null){
                    self::$instance = new TokenManager();
                }
            
                return self::$instance;
        }

        function generateToken($userID): string{
                $iv = openssl_random_pseudo_bytes(16);
                

                $token = openssl_encrypt(strval($userID), $this->algo, $this->secretKey, 0, 16);

                $_SESSION[strval($userID)] = $token;
                
                return $token;
        }

        function isTokenValid($token){
            $iv = openssl_random_pseudo_bytes(16);
            
            $userID = openssl_decrypt($token, $this->algo, $this->secretKey, 0, 16);
            
            return isset($_SESSION[$userID]) ? true: false;
         //   return isset($this->tokensList[$userID]) && $this->tokensList[$userID] === $token; 
        }

        function decrypt($token){

            $userID = openssl_decrypt($token, $this->algo, $this->secretKey, 0, 16);
            
            return $userID;
        }

        function getTokensList(): array{
            
            return $_SESSION;
        }
    }

?>*/