import { useEmployees } from '../model/useEmployees';
import { EmployeeModal } from './EmployeeModal';

export const EmployeeManagement = ({ title, controller }: { title: string, controller: any }) => {
  const { employees, isModalOpen, setIsModalOpen, addEmployee, removeEmployee, isLoading } = controller;

  return (
    <div className="w-full">
      <div className="flex justify-between items-center mb-8">
        <h2 className="text-2xl font-bold">Управление командой</h2>
        <button
          onClick={() => setIsModalOpen(true)}
          className="bg-orange-500 hover:bg-orange-600 px-5 py-2 rounded-xl text-white font-medium transition-all shadow-lg shadow-orange-500/10"
        >
          + Новый сотрудник
        </button>
      </div>

      <div className="bg-app-surface rounded-2xl border border-gray-800 overflow-hidden">
        <table className="w-full text-left border-collapse">
          <thead className="bg-header-bg text-[11px] uppercase tracking-wider">
            <tr>
              <th className="p-4 font-semibold">Имя</th>
              <th className="p-4 font-semibold">Email</th>
              <th className="p-4 font-semibold text-center">Статус</th>
              <th className="p-4 font-semibold text-right">Удалить</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-800">
            {employees.map(user => (
              <tr key={user.id} className="hover:bg-[#252525]/50 transition-colors text-gray-200">
                <td className="p-4 font-medium">{user.name}</td>
                <td className="p-4 text-gray-400">{user.email}</td>
                <td className="p-4 text-center">
                  <span className={`px-2 py-1 rounded-lg text-[10px] font-bold uppercase ${
                    user.status === 'activated' ? 'bg-green-500/10 text-green-500' : 'bg-red-500/10 text-red-500'
                  }`}>
                    {user.status}
                  </span>
                </td>
                <td className="p-4 text-right">
                  <button
                    onClick={() => removeEmployee(user.id)}
                    className="p-2 hover:bg-red-500/10 rounded-lg group transition-all"
                  >
                    <span className="text-red-500/60 group-hover:text-red-500 text-sm">Удалить</span>
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {employees.length === 0 && (
          <div className="p-20 text-center text-gray-600">Список сотрудников пуст</div>
        )}
      </div>

      <EmployeeModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSave={addEmployee}
        loading={isLoading}
      />
    </div>
  );
};
