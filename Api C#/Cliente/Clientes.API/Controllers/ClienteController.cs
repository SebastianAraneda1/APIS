using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using Clientes.API.Models;
// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace Clientes.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ClienteController : ControllerBase
    {
        private static IList<Cliente> lista = new List<Cliente>();
        // GET: api/<ClienteController>
        [HttpGet]
        public IEnumerable<Cliente> Get()
        {
            return lista;
        }

        // GET api/<ClienteController>/5
        [HttpGet("{id}")]
        public Cliente Get(int id)
        {
            //X VA A SER IGUAL AL RESULTADO DONDE EL X.ID SEA IGUAL AL ID QUE VA A RECIBIR LA FUNCIÓN
            //EL FIRSTOFDEAFULT VA A DEVOLVER EL PRIMER VALOR QUE COINCIDA CON LO QUE PIDES, SINO LO ENCUENTRA VA A TRAER UNO POR DEFECTO
            Cliente resultado = lista.FirstOrDefault(x => x.id == id);

            //OTRA ALTERNATIVA USANDO SQL
            var lista2 = (from x in lista 
                          where x.id == id 
                          select x);
            return resultado;
        }

        // POST api/<ClienteController>
        [HttpPost]
        public void Post([FromBody] Cliente value)
        {
            lista.Add(value);
        }

        // PUT api/<ClienteController>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] Cliente value)
        {
            Cliente selection = lista.FirstOrDefault(x => x.id == id);
            //Va a buscar la posición del id que encontro
            lista[lista.IndexOf(selection)] = value;
        }

        // DELETE api/<ClienteController>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
            Cliente selection = lista.FirstOrDefault(x => x.id == id);
            lista.Remove(selection);
        }
    }
}
