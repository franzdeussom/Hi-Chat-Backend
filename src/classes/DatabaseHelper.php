<?php


class DatabaseHelper
{
    // production parameters
    private static ?DatabaseHelper $instance = null;
    private static string $host = "localhost";
    private static string $dbname = "HiChat";
    private static string $user = "root";
    private static string $password = "";
    protected PDO $db;

    private function __construct()
    {
        try {
            $this->db = new PDO(sprintf("mysql:host=%s;dbname=%s;charset=utf8", self::$host, self::$dbname),
                self::$user,
                self::$password,
                array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
        } catch (Exception $e) {
            echo "Something went wrong<br>";
            die($e->getMessage());
        }
    }

    /**
     * @return DatabaseHelper
     */
    public static function getInstance(): DatabaseHelper
    {
        self::$instance = self::$instance ?? new self();
        return self::$instance;
    }

    /**
     * configure default parameter to use when connecting to database
     * @param string $host
     * @param string $dbname
     * @param string $user
     * @param string $password
     * @return void
     */
    public static function configure(string $host, string $dbname, string $user, string $password): void
    {
        if ($_SERVER['REQUEST_SCHEME'] == 'http') {
            self::$host = $host;
            self::$dbname = $dbname;
            self::$user = $user;
            self::$password = $password;
        }
    }

    /**
     * Define the fetchMode
     * @param int $fetchMode fetchMode
     */
    public function setFetchMode(int $fetchMode): void
    {
        $this->db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, $fetchMode);
    }

    /**
     * check if field exists
     * @param string $table
     * @param string $field
     * @return bool
     */
    public function fieldExists(string $table, string $field): bool
    {
        try {
            $this->fetch("SELECT $field FROM $table LIMIT 1");
            return true;
        } catch (Exception $e) {
            return false;
        }
    }

    /**
     * Execute an SQL query and return row(s) of the result
     * @param string $request SQL query
     * @param array|null $values Optional values
     * @param bool $all Query with several rows or not
     * @return array|mixed Return data
     */
    public function fetch(string $request, array $values = null, bool $all = true): mixed
    {
        $results = self::exec($request, $values);
        return ($all) ? $results->fetchAll() : $results->fetch();
    }

    /**
     * Execute an SQL query and return the result (prepared request or not)
     * @param string $request SQL query
     * @param array|null $values Optional values
     * @return PDOStatement
     */
    private function exec(string $request, array $values = null): PDOStatement
    {
        $req = $this->db->prepare($request);
        $req->execute($values);
        return $req;
    }

    /**
     * Execute an SQL query and return the status
     * @param string $request SQL query
     * @param array $values Optional values
     * @return bool Result of the request
     */
    public function execute(string $request, array $values = array()): bool
    {
        return (bool)self::exec($request, $values);
    }

    /**
     * @return PDO
     */
    public function getDb(): PDO
    {
        return $this->db;
    }

}
