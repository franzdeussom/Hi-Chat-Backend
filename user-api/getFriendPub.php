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

    }else{
        http_response_code(403);
    }

    $query = $conn->prepare("SELECT DISTINCT 
                                        PUBLICATION.id_pub,
                                        PUBLICATION.id_user, 
                                        PUBLICATION.libelle, 
                                        PUBLICATION.date_pub, 
                                        PUBLICATION.url_file, 
                                        PUBLICATION.is_public, 
                                        PUBLICATION.colorBg, 
                                        PUBLICATION.PID,
                                        PUBLICATION.type_pub,
                                        USERS.nom, 
                                        USERS.prenom, 
                                        USERS.profilImgUrl, 
                                        (SELECT COUNT(*) 
                                            FROM HiChat.PUB_LIKE
                                            WHERE 
                                                PUB_LIKE.id_pub = PUBLICATION.id_pub
                                        ) as 'nbrLike',
                                        (SELECT COUNT(*) 
                                            FROM HiChat.PUB_LIKE 
                                            WHERE 
                                                PUB_LIKE.id_users = :id_users
                                                AND 
                                                PUB_LIKE.id_pub = PUBLICATION.id_pub
                                        ) as 'alreadyLike',
                                        (SELECT COUNT(*) 
                                            FROM HiChat.COMMENTAIRE
                                            WHERE 
                                                COMMENTAIRE.id_publication = PUBLICATION.id_pub
                    
                                        ) as 'nbrCommentaire' 

                                        FROM HiChat.PUBLICATION,
                                        HiChat.USERS, 
                                        HiChat.FOLLOW 
                                            WHERE 
                                                (SELECT COUNT(*) 
                                                    FROM HiChat.PUB_LIKE 
                                                    WHERE PUB_LIKE.id_users = :id_users 
                                                    AND 
                                                    PUB_LIKE.id_pub = PUBLICATION.id_pub
                                                ) = 0 
                                                AND
                                                FOLLOW.id_users_WF = :id_users 
                                            AND 
                                                FOLLOW.id_users_F = USERS.id_users                                           
                                            AND                                            
                                                PUBLICATION.id_user = USERS.id_users
                                            ORDER BY PUBLICATION.id_pub DESC LIMIT 110
                            ");
    $query->execute([
        ':id_users' => $data->id_users
    ]);

    $row = $query->rowCount();

    if($row > 0){
        $response = json_encode($query->fetchAll());
        echo $response;
    }else{
        echo json_encode([]);
    }
?>
