using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace GUIPresentation
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            Consulter my_consulter = new Consulter();
            my_consulter.getQuerys();
            List<DataTable> result = new List<DataTable>();
            result = my_consulter.getQuerys();
            DataTable day_avg = new DataTable();
            DataTable ser_avg = new DataTable();
            DataTable gen_avg = new DataTable();
            day_avg = result[0];


            mainSummary.DisplayMemberPath = "Download";
            mainSummary.SelectedValuePath = "Date";
            mainSummary.ItemsSource = day_avg.DefaultView;
        }
    }
}
