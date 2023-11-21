from fastapi import Path, APIRouter
from starlette import status

from app.services.demo.models import ObtenerMedicosResponse
from app.services.demo.service import DemoService

demo_router = APIRouter()


@demo_router.get(
    '/',
    response_model=ObtenerMedicosResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener todos los médicos",
    response_description="Devuelve un listado completo de médicos",
)
async def obtener_medicos():
    """
    Obtiene un listado de todos los médicos registrados en la base de datos.

    ### Descripción

    Esta operación recupera una lista completa de médicos, incluyendo sus detalles personales y profesionales. Es útil para obtener una visión general de todos los profesionales médicos registrados en el sistema.

    ### Campos de respuesta (`Array/Listado`):
    - **idmedico**: int - El identificador único de cada médico.
    - **nombre**: str - Nombres del médico.
    - **apellidos**: str - Apellidos del médico.
    - **ruc**: str - Registro Único de Contribuyentes (RUC), único para cada médico.
    - **direccion**: str - Dirección residencial del médico.
    - **correo**: str - Correo electrónico del médico.
    - **telefono**: str - Número de teléfono celular del médico.
    - **id_ciudad**: int - Identificador de la ciudad donde reside el médico.

    ### Detalles Técnicos

    - **Consulta SQL**: `SELECT * FROM medicos`
    - **Método HTTP**: GET
    - **Ruta**: `/medicos`

    ### Notas Adicionales

    - Esta consulta no requiere parámetros.
    - Asegúrese de tener los permisos adecuados antes de realizar esta consulta.
    """

    return DemoService.obtener_medicos()


@demo_router.get(
    '/{i_nombre_medico}',
    response_model=ObtenerMedicosResponse,
    status_code=status.HTTP_200_OK,
    summary="Filtrar médicos por nombre",
    response_description="Devuelve un listado de médicos filtrados por nombre",
)
async def obtener_medicos_filtro(
        i_nombre_medico: str = Path(..., description="Nombre del médico para filtrar resultados")
):
    """
    ### Descripción

    Filtrar médicos por nombre en la base de datos.

    ### Campos

    - **idmedico**: Identificador único del médico.
    - **nombre**: Nombres del médico.
    - **apellidos**: Apellidos del médico.
    - **ruc**: RUC del médico (único por cada registro).
    - **direccion**: Dirección residencial del médico.
    - **correo**: Correo electrónico del médico.
    - **telefono**: Teléfono celular del médico.
    - **id_ciudad**: Código identificador de la ciudad donde reside el médico.
    """
    return DemoService.obtene_medicos_filtro(i_nombre_medico)
