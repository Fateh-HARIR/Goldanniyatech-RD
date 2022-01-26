using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


using UnityEngine;

public class SQLRequest : MonoBehaviour
{


    //Connection to a SQL Server (Not working because no SQL Server is up & running in this machine)
    string connectionString = @"Data Source=; Initial Catalog=; User ID=; Password=";

    SqlConnection cnn;
    //connectionString = @"Data Source=; Initial Catalog=; User ID=; Password="; 


    // Start is called before the first frame update
    void Start()
    {
        cnn = new SqlConnection(connectionString);
        cnn.Open();
        Debug.Log("Connection Open!");
        cnn.Close(); 
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
