<?php
    require('../connectDB.php');
    require('../header.php');
    require('../TokenManager.php');
    require('../autoload.php');

    global $conn;

    $getData = file_get_contents('php://input');

    if(isset($getData) && !empty($getData)){
        $data = json_decode($getData);
        http_response_code(200);
    }else{
        return;
    }

    if(verifiedToken($_SERVER['HTTP_AUTHORIZATION'])){
            $query = $conn->prepare('INSERT INTO HiChat.FOLLOW( 
                            id_users_WF,
                            id_users_F
                           ) 
                            VALUES(
                                :id_users_WF,
                                :id_users_F
                            )');

            $query->execute([
                ':id_users_WF' => $data->id_WF,
                ':id_users_F' => $data->id_F
            ]);

            if($query){
                $response = [
                    'success' => true,
                    'valid' => true
                ];
                echo json_encode($response);
            }else{
                echo json_encode([]);
            }
    }else{
        http_response_code(403);
    }

    
?>
