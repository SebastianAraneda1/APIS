﻿using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using Clientes.API.Models;
using InversionesLtda.API.Models;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace Clientes.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProductoController : ControllerBase
    {
        private static IList<Producto> listaProductos = new List<Producto>();

        // GET: api/<ProductoController>
        //Obtener todos los productos
        [HttpGet]
        public IEnumerable<Producto> Get()
        {
            return listaProductos;
        }

        // GET api/<ProductoController>/5
        [HttpGet("{id}")]
        public Producto Get(int id)
        {
            Producto idSeleccionado = listaProductos.FirstOrDefault(x => x.id == id);

            return idSeleccionado;
        }

        // POST api/<ProductoController>
        [HttpPost]
        public void Post([FromBody] Producto value)
        {
            listaProductos.Add(value);
        }

        // PUT api/<ProductoController>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] Producto value)
        {
            Producto idSeleccionado = listaProductos.FirstOrDefault(x => x.id == id);

            listaProductos[listaProductos.IndexOf(idSeleccionado)] = value;
        }

        // DELETE api/<ProductoController>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
            Producto idSeleccionado = listaProductos.FirstOrDefault(x => x.id == id);

            listaProductos.Remove(idSeleccionado);
        }
        
        [HttpPost("descontar")]
        public ResponseDTO descontarStock([FromBody] DescontarStockRequest request){
            ResponseDTO response = new ResponseDTO();
            response.status = 500;
            response.message = "NoOK";
            try
            {
                Producto productoSolicitado = listaProductos.FirstOrDefault(x => x.id == request.IdProducto);

                if (productoSolicitado != null)
                {
                    if (productoSolicitado.cantidad > request.CantidadProducto)
                    {
                        int cantidad = productoSolicitado.cantidad - request.CantidadProducto;
                        listaProductos[listaProductos.IndexOf(productoSolicitado)].cantidad = cantidad;
                        response.status = 200;
                        response.message = "OK";
                    }
                }
                return response;
            }
            catch (System.Exception err)
            {
                Console.WriteLine(err);
                return response;
            }

        }
    }
}
