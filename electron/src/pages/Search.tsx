import React, { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Search as SearchIcon, File } from 'lucide-react'
import { searchApi } from '@/utils/api'
import { formatBytes } from '@/utils/formatBytes'

export default function Search() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<any[]>([])
  const [loading, setLoading] = useState(false)
  const [searched, setSearched] = useState(false)

  const handleSearch = async () => {
    if (!query.trim()) return

    setLoading(true)
    setSearched(true)

    try {
      const response = await searchApi.search(query)
      setResults(response.data.results)
    } catch (err) {
      console.error('Error searching:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSearch()
    }
  }

  return (
    <div className="p-8 space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Search Files</h1>
        <p className="text-slate-600">Find files quickly across your system</p>
      </div>

      <Card>
        <CardContent className="pt-6">
          <div className="flex gap-4">
            <Input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Search by filename, extension, or content..."
              className="flex-1"
            />
            <Button
              onClick={handleSearch}
              disabled={loading || !query.trim()}
              className="bg-blue-500 hover:bg-blue-600"
            >
              <SearchIcon className="mr-2 h-4 w-4" />
              Search
            </Button>
          </div>
        </CardContent>
      </Card>

      {loading && (
        <div className="flex justify-center items-center py-12">
          <div className="text-slate-500">Searching...</div>
        </div>
      )}

      {searched && !loading && (
        <Card>
          <CardHeader>
            <CardTitle>
              {results.length} Results {query && `for "${query}"`}
            </CardTitle>
          </CardHeader>
          <CardContent>
            {results.length === 0 ? (
              <div className="text-center py-12 text-slate-500">
                No files found matching your search
              </div>
            ) : (
              <div className="space-y-2">
                {results.map((file, idx) => (
                  <div
                    key={idx}
                    className="flex items-center gap-4 p-4 bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors"
                  >
                    <File className="h-8 w-8 text-blue-500" />
                    <div className="flex-1 min-w-0">
                      <div className="font-medium truncate">{file.filename}</div>
                      <div className="text-sm text-slate-600 truncate">{file.path}</div>
                    </div>
                    <div className="text-sm text-slate-500">
                      {formatBytes(file.size)}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </CardContent>
        </Card>
      )}
    </div>
  )
}
