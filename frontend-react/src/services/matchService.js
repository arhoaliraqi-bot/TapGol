// services/matchService.js
import api from './api';

class MatchService {
  async getGroupMatches(groupId) {
    const response = await api.get(`/matches/group/${groupId}`);
    return response.data;
  }

  async getUserMatches() {
    const response = await api.get('/matches/user');
    return response.data;
  }

  async getMatch(matchId) {
    const response = await api.get(`/matches/${matchId}`);
    return response.data;
  }

  async createMatch(data) {
    const response = await api.post('/matches', data);
    return response.data;
  }

  async joinMatch(matchId) {
    const response = await api.post(`/matches/${matchId}/join`);
    return response.data;
  }

  async leaveMatch(matchId) {
    const response = await api.post(`/matches/${matchId}/leave`);
    return response.data;
  }
}

export default new MatchService();
