<?php
$hote = 'localhost'; $base = 'dlc_logs'; $user = 'dlc_admin'; $mdp = 'Password123!';
try {
    $pdo = new PDO("mysql:host=$hote;dbname=$base;charset=utf8", $user, $mdp, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
    ]);
} catch (PDOException $e) {
    die("Erreur de connexion : " . $e->getMessage());
}
?>
