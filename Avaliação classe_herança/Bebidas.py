
class Bebida:
     string Nome { get; set; }
     double VolumeLitros { get; set; }
     double Preco { get; set; }

     Bebida(string nome, double volumeLitros, double preco)
    {
        Nome = nome;
        VolumeLitros = volumeLitros;
        Preco = preco;
    }

    public virtual void Descrever()
    {
        Console.WriteLine("Bebida: {Nome}");
        Console.WriteLine("Volume: {VolumeLitros} litros");
        Console.WriteLine("Preço: R$ {Preco:F2}");
    }

class Refrigerante : Bebida
{
     string Sabor { get; set; }
     bool Diet { get; set; }

     Refrigerante(string nome, double volumeLitros, double preco, string sabor, bool diet)
        : base(nome, volumeLitros, preco)
    {
        Sabor = sabor;
        Diet = diet;
    }

     override void Descrever()
    {
        base.Descrever();
        Console.WriteLine("Sabor: {Sabor}");
        Console.WriteLine("Diet: {(Diet ? "Sim" : "Não")}");
    }
}

 class Suco : Bebida
{
     string Sabor { get; set; }
     bool Natural { get; set; }

     Suco(string nome, double volumeLitros, double preco, string sabor, bool natural)
        : base(nome, volumeLitros, preco)
    {
        Sabor = sabor;
        Natural = natural;
    }

     override void Descrever()
    {
        base.Descrever();
        Console.WriteLine("Sabor: {Sabor}");
        Console.WriteLine("Natural: {(Natural ? "Sim" : "Não")}");
    }
}

class Café(Bebida)
     string Tipo { get; set; }
     bool Cafeinado { get; set; }

     Café(string nome, double volumeLitros, double preco, string tipo, bool cafeinado)
        : base(nome, volumeLitros, preco)
    {
        Tipo = tipo;
        Cafeinado = cafeinado;
    }

     override void Descrever()
    {
        base.Descrever();
        Console.WriteLine("Tipo: {Tipo}");
        Console.WriteLine("Cafeinado: {(Cafeinado ? "Sim" : "Não")}");
    }
}

 class cerveja : Bebida
{
     string Tipo { get; set; }
     bool Comalcool { get; set; }

     cerveja(string nome, double volumeLitros, double preco, string tipo, bool Comalcool)
        : base(nome, volumeLitros, preco)
    {
        Tipo = tipo;
        Comalcool = Comalcool;
    }

     override void Descrever()
    {
        base.Descrever();
        Console.WriteLine("Tipo: {Tipo}");
        Console.WriteLine("Comalcool: {(Comalcool ? "Sim" : "Não")}");
    }
}

{
using System;

class Program
{
    static void Main()
    {
        Bebida bebida1 = new Refrigerante("Coca-Cola", 2.0, 3.5, "Cola", false);
        Bebida bebida2 = new Suco("Suco de Laranja", 0.5, 2.0, "Laranja", true);
        Bebida bebida3 = new Café("Café Expresso", 0.1, 2.5, "Expresso", true);
        Bebida bebida4 = new Café("Cerveja", 0.1, 2.5, "Comalco", true);

        bebida1.Descrever();
        Console.WriteLine();

        bebida2.Descrever();
        Console.WriteLine();

        bebida3.Descrever();
    }
}
