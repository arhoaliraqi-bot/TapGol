// services/notificationService.js
import api from './api';

class NotificationService {
  async getNotifications() {
    const response = await api.get('/notifications');
    return response.data;
  }

  async markAsRead(notificationId) {
    const response = await api.put(`/notifications/${notificationId}/read`);
    return response.data;
  }

  async markAllAsRead() {
    const response = await api.put('/notifications/mark-all-read');
    return response.data;
  }

  async deleteNotification(notificationId) {
    const response = await api.delete(`/notifications/${notificationId}`);
    return response.data;
  }
}

export default new NotificationService();
