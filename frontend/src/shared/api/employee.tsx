import type { Employee, CreateEmployeeDto, GetAllEmployeesResponse } from '@/shared/types/employee';

// Используем константу, которую собрал Vite в конфиге
const API_URL = `${__API_URL__}/employee`;


export const employeeApi = {
  getAll: (businessId: string): Promise<GetAllEmployeesResponse> =>
    fetch(`${API_URL}/get_all`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ business_id: businessId })
    }).then(r => r.json()),

  create: (data: CreateEmployeeDto) =>
    fetch(`${API_URL}/create`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    }),

  delete: (id: string) =>
    fetch(`${API_URL}/delete`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id }),
    }),
};
