﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace InversionesLtda.API.Models
{
    public class Cliente
    {
        public int id { get; set; }
        public string nombre { get; set; }
        public string rut { get; set; }
        public string direccion { get; set; }
        public string correo { get; set; }
    }
}
