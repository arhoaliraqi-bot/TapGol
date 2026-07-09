// services/themeService.js
import api from './api';

class ThemeService {
  async getUserThemes() {
    const response = await api.get('/themes/user');
    return response.data;
  }

  async createTheme(data) {
    const response = await api.post('/themes/user', data);
    return response.data;
  }

  async activateTheme(themeId) {
    const response = await api.put(`/themes/user/${themeId}/activate`);
    return response.data;
  }

  async deleteTheme(themeId) {
    const response = await api.delete(`/themes/user/${themeId}`);
    return response.data;
  }

  async getGroupTheme(groupId) {
    const response = await api.get(`/themes/group/${groupId}`);
    return response.data;
  }

  async setGroupTheme(groupId, backgroundImage) {
    const response = await api.post(`/themes/group/${groupId}`, {
      background_image: backgroundImage
    });
    return response.data;
  }

  async deleteGroupTheme(groupId) {
    const response = await api.delete(`/themes/group/${groupId}`);
    return response.data;
  }
}

export default new ThemeService();
