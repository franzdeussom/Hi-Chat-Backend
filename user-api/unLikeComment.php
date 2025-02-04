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
        if(!isset($data->id_commentaire) && empty($data->id_commentaire)){
                        $query = $conn->prepare('DELETE FROM HiChat.COMMENT_LIKE 
                                        WHERE
                                            COMMENT_LIKE.id_comment = (SELECT COMMENTAIRE.id_commentaire FROM HiChat.COMMENTAIRE WHERE COMMENTAIRE.PID = :PID)
                                            AND
                                            COMMENT_LIKE.id_users = :id_users
                                        ');
                        $query->execute([
                            ':PID' => $data->PID,
                            ':id_users' => $data->id_users
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
                        $query = $conn->prepare('DELETE FROM HiChat.COMMENT_LIKE 
                                        WHERE
                                            COMMENT_LIKE.id_like_comment = :idCommentLike
                                            AND
                                            COMMENT_LIKE.id_users = :id_users
                                        ');
                        $query->execute([
                            ':idCommentLike' => $data->id_commentaire,
                            ':id_users' => $data->id_users
                        ]);

                if($query){
                    $response = [
                        'success' => true,
                        'valid' => true
                    ];
                    echo json_encode($response);
            }
        }
  }else{
      http_response_code(403);
  }
    
?>
