import axios from 'axios';

const API_BASE = 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_BASE,
  timeout: 60000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const fileApi = {
  async analyzeFolder(folderPath: string, recursive: boolean = true) {
    return api.post('/files/analyze', { folder_path: folderPath, recursive });
  },

  async getFiles(folderPath: string, skip: number = 0, limit: number = 100) {
    return api.get('/files/list', { params: { folder_path: folderPath, skip, limit } });
  },

  async organizeFiles(plan: any) {
    return api.post('/files/organize', { plan });
  },

  async moveFile(source: string, destination: string) {
    return api.post('/files/move', { source, destination });
  },
};

export const searchApi = {
  async search(query: string, filters?: any) {
    return api.get('/search', { params: { q: query, ...filters } });
  },

  async getHistory(limit: number = 10) {
    return api.get('/search/history', { params: { limit } });
  },
};

export const tagsApi = {
  async createTag(name: string, color: string = '#3B82F6') {
    return api.post('/tags', { name, color });
  },

  async getAllTags() {
    return api.get('/tags');
  },

  async tagFile(fileId: number, tagId: number) {
    return api.post('/tags/file', { file_id: fileId, tag_id: tagId });
  },

  async untagFile(fileId: number, tagId: number) {
    return api.delete('/tags/file', { params: { file_id: fileId, tag_id: tagId } });
  },

  async getFileTags(fileId: number) {
    return api.get(`/tags/file/${fileId}`);
  },

  async getFilesByTag(tagId: number) {
    return api.get(`/tags/${tagId}/files`);
  },

  async deleteTag(tagId: number) {
    return api.delete(`/tags/${tagId}`);
  },
};

export const duplicatesApi = {
  async findDuplicates() {
    return api.get('/duplicates');
  },

  async deleteDuplicates(fileIds: number[]) {
    return api.post('/duplicates/delete', { file_ids: fileIds });
  },
};

export const analyticsApi = {
  async getStats() {
    return api.get('/analytics/stats');
  },

  async getDistribution() {
    return api.get('/analytics/distribution');
  },
};
