import React, { useState, useEffect } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { Copy, Trash2, AlertCircle } from 'lucide-react'
import { duplicatesApi } from '@/utils/api'
import { formatBytes } from '@/utils/formatBytes'

export default function Duplicates() {
  const [duplicates, setDuplicates] = useState<any>(null)
  const [loading, setLoading] = useState(true)
  const [selectedFiles, setSelectedFiles] = useState<Set<number>>(new Set())

  useEffect(() => {
    findDuplicates()
  }, [])

  const findDuplicates = async () => {
    setLoading(true)
    try {
      const response = await duplicatesApi.findDuplicates()
      setDuplicates(response.data)
    } catch (err) {
      console.error('Error finding duplicates:', err)
    } finally {
      setLoading(false)
    }
  }

  const toggleFileSelection = (fileId: number) => {
    const newSelected = new Set(selectedFiles)
    if (newSelected.has(fileId)) {
      newSelected.delete(fileId)
    } else {
      newSelected.add(fileId)
    }
    setSelectedFiles(newSelected)
  }

  const handleDeleteSelected = async () => {
    if (selectedFiles.size === 0) return

    if (!confirm(`Are you sure you want to delete ${selectedFiles.size} duplicate files?`)) {
      return
    }

    try {
      await duplicatesApi.deleteDuplicates(Array.from(selectedFiles))
      setSelectedFiles(new Set())
      findDuplicates()
    } catch (err) {
      console.error('Error deleting duplicates:', err)
      alert('Failed to delete some files')
    }
  }

  if (loading) {
    return (
      <div className="p-8">
        <div className="text-center py-12 text-slate-500">Scanning for duplicates...</div>
      </div>
    )
  }

  const duplicateGroups = duplicates?.duplicates ? Object.values(duplicates.duplicates) : []

  return (
    <div className="p-8 space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Duplicate Files</h1>
        <p className="text-slate-600">Find and remove duplicate files to free up space</p>
      </div>

      {duplicates && (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-medium">Duplicate Groups</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{duplicates.duplicate_groups}</div>
              <p className="text-xs text-slate-500">groups found</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-medium">Duplicate Files</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{duplicates.total_duplicate_count}</div>
              <p className="text-xs text-slate-500">duplicate files</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-medium">Wasted Space</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-red-600">
                {formatBytes(duplicates.total_wasted_space)}
              </div>
              <p className="text-xs text-slate-500">can be freed</p>
            </CardContent>
          </Card>
        </div>
      )}

      {selectedFiles.size > 0 && (
        <Alert>
          <AlertDescription>
            <div className="flex items-center justify-between">
              <span>{selectedFiles.size} files selected</span>
              <Button
                variant="destructive"
                size="sm"
                onClick={handleDeleteSelected}
              >
                <Trash2 className="mr-2 h-4 w-4" />
                Delete Selected
              </Button>
            </div>
          </AlertDescription>
        </Alert>
      )}

      {duplicateGroups.length === 0 ? (
        <Card>
          <CardContent className="py-12">
            <div className="text-center text-slate-500">
              <Copy className="h-12 w-12 mx-auto mb-4 text-slate-400" />
              <p className="text-lg">No duplicate files found</p>
              <p className="text-sm">Your file system is clean!</p>
            </div>
          </CardContent>
        </Card>
      ) : (
        <div className="space-y-4">
          {duplicateGroups.map((group: any, groupIdx: number) => (
            <Card key={groupIdx}>
              <CardHeader>
                <div className="flex items-center justify-between">
                  <CardTitle className="text-lg">
                    Duplicate Group {groupIdx + 1}
                  </CardTitle>
                  <div className="text-sm text-slate-600">
                    {group.count} files - {formatBytes(group.wasted_space)} wasted
                  </div>
                </div>
              </CardHeader>
              <CardContent>
                <div className="space-y-2">
                  {group.files.map((file: any, fileIdx: number) => (
                    <div
                      key={fileIdx}
                      className={`flex items-center gap-4 p-3 rounded-lg border ${
                        selectedFiles.has(file.id)
                          ? 'bg-red-50 border-red-200'
                          : 'bg-slate-50 border-slate-200'
                      }`}
                    >
                      <input
                        type="checkbox"
                        checked={selectedFiles.has(file.id)}
                        onChange={() => toggleFileSelection(file.id)}
                        className="h-4 w-4"
                        disabled={fileIdx === 0}
                      />
                      <div className="flex-1 min-w-0">
                        <div className="font-medium truncate">{file.filename}</div>
                        <div className="text-sm text-slate-600 truncate">{file.path}</div>
                      </div>
                      <div className="text-sm text-slate-500">
                        {formatBytes(file.size)}
                      </div>
                      {fileIdx === 0 && (
                        <div className="text-xs bg-green-100 text-green-700 px-2 py-1 rounded">
                          Keep
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  )
}
