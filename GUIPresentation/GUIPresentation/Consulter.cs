using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using SQLHandling;

namespace GUIPresentation
{
    class Consulter
    {
        
        private string my_path = "";
        private string my_file = "";
        private DataTable day_avg = new DataTable();
        private DataTable ser_avg = new DataTable();
        private DataTable gen_avg = new DataTable();
        


        DBConnection connection;
        public Consulter()
        {
            this.my_path=Directory.GetCurrentDirectory();
            this.my_path = this.my_path.Substring(0, this.my_path.Length - 56)+"data";
            this.my_path = this.my_path.Replace("\\", "/");
            
            this.my_file = "record.db";
            this.connection= new DBConnection(this.my_path,this.my_file);

            connection.Connecter();
        }

        public List<DataTable> getQuerys()
        {
            List<string> querys = new List<string> { "SELECT * FROM day_avg", "SELECT * FROM ser_avg", "SELECT * FROM gen_avg" };
            List<DataTable> tables = new List<DataTable> { this.day_avg, this.ser_avg, this.gen_avg };
            return this.connection.Consulter(querys, tables);
        }
    }
}
