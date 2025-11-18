import React, { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { CheckCircle, AlertCircle, Loader, FolderOpen } from 'lucide-react'
import { fileApi } from '@/utils/api'
import { formatBytes } from '@/utils/formatBytes'

export default function Organizer() {
  const [selectedFolder, setSelectedFolder] = useState('')
  const [loading, setLoading] = useState(false)
  const [plan, setPlan] = useState<any>(null)
  const [executing, setExecuting] = useState(false)
  const [result, setResult] = useState<any>(null)

  const handleFolderSelect = () => {
    const input = document.createElement('input')
    input.type = 'file'
    input.setAttribute('webkitdirectory', '')
    input.setAttribute('directory', '')

    input.onchange = (e: any) => {
      const files = e.target.files
      if (files.length > 0) {
        const path = files[0].path
        // BUGFIX: Use Math.max to handle both forward and backward slashes correctly
        const lastSlashIndex = Math.max(path.lastIndexOf('/'), path.lastIndexOf('\\'))
        const folderPath = lastSlashIndex >= 0 ? path.substring(0, lastSlashIndex) : path
        setSelectedFolder(folderPath)
      }
    }

    input.click()
  }

  const analyzeFolder = async () => {
    if (!selectedFolder) return

    setLoading(true)
    setPlan(null)
    setResult(null)

    try {
      const response = await fileApi.analyzeFolder(selectedFolder)
      setPlan(response.data.plan)
    } catch (err: any) {
      console.error('Error analyzing folder:', err)
      alert('Error analyzing folder: ' + (err.response?.data?.detail || err.message))
    } finally {
      setLoading(false)
    }
  }

  const executePlan = async () => {
    if (!plan) return

    setExecuting(true)

    try {
      const response = await fileApi.organizeFiles(plan)
      setResult(response.data.results)
    } catch (err: any) {
      console.error('Error executing plan:', err)
      alert('Error executing plan: ' + (err.response?.data?.detail || err.message))
    } finally {
      setExecuting(false)
    }
  }

  return (
    <div className="p-8 space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">File Organizer</h1>
        <p className="text-slate-600">Analyze and organize your files intelligently</p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Step 1: Select Folder</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex gap-4">
            <Input
              value={selectedFolder}
              onChange={(e) => setSelectedFolder(e.target.value)}
              placeholder="Enter folder path or click browse"
              className="flex-1"
            />
            <Button onClick={handleFolderSelect}>
              <FolderOpen className="mr-2 h-4 w-4" />
              Browse
            </Button>
          </div>
          <Button
            onClick={analyzeFolder}
            disabled={!selectedFolder || loading}
            className="w-full bg-blue-500 hover:bg-blue-600"
          >
            {loading ? (
              <>
                <Loader className="mr-2 h-4 w-4 animate-spin" />
                Analyzing...
              </>
            ) : (
              'Analyze Folder'
            )}
          </Button>
        </CardContent>
      </Card>

      {plan && (
        <Card>
          <CardHeader>
            <CardTitle>Step 2: Review Organization Plan</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-3 gap-4">
              <div className="text-center p-4 bg-blue-50 rounded-lg">
                <div className="text-2xl font-bold text-blue-700">{plan.total_files}</div>
                <div className="text-sm text-slate-600">Total Files</div>
              </div>
              <div className="text-center p-4 bg-green-50 rounded-lg">
                <div className="text-2xl font-bold text-green-700">{plan.summary.to_move}</div>
                <div className="text-sm text-slate-600">To Organize</div>
              </div>
              <div className="text-center p-4 bg-purple-50 rounded-lg">
                <div className="text-2xl font-bold text-purple-700">
                  {plan.total_files - plan.summary.to_move}
                </div>
                <div className="text-sm text-slate-600">Already Organized</div>
              </div>
            </div>

            {plan.operations.length > 0 && (
              <div className="mt-4">
                <h3 className="font-semibold mb-2">Preview Changes:</h3>
                <div className="max-h-64 overflow-y-auto space-y-2">
                  {plan.operations.slice(0, 10).map((op: any, idx: number) => (
                    <div key={idx} className="text-sm p-2 bg-slate-50 rounded">
                      <div className="font-medium truncate">{op.source}</div>
                      <div className="text-slate-600 truncate">→ {op.destination}</div>
                    </div>
                  ))}
                  {plan.operations.length > 10 && (
                    <div className="text-sm text-slate-500 text-center">
                      ... and {plan.operations.length - 10} more files
                    </div>
                  )}
                </div>
              </div>
            )}

            <Button
              onClick={executePlan}
              disabled={executing || plan.summary.to_move === 0}
              className="w-full bg-green-500 hover:bg-green-600"
            >
              {executing ? (
                <>
                  <Loader className="mr-2 h-4 w-4 animate-spin" />
                  Organizing...
                </>
              ) : (
                <>
                  <CheckCircle className="mr-2 h-4 w-4" />
                  Execute Organization
                </>
              )}
            </Button>
          </CardContent>
        </Card>
      )}

      {result && (
        <Alert variant={result.failed === 0 ? "default" : "destructive"}>
          <AlertDescription>
            <div className="space-y-2">
              <div className="font-semibold">
                {result.failed === 0 ? 'Organization Completed Successfully!' : 'Organization Completed with Errors'}
              </div>
              <div>Succeeded: {result.succeeded}</div>
              {result.failed > 0 && <div>Failed: {result.failed}</div>}
              {result.errors.length > 0 && (
                <div className="mt-2">
                  <div className="font-semibold">Errors:</div>
                  {result.errors.slice(0, 5).map((err: any, idx: number) => (
                    <div key={idx} className="text-sm">
                      {err.file}: {err.error}
                    </div>
                  ))}
                </div>
              )}
            </div>
          </AlertDescription>
        </Alert>
      )}
    </div>
  )
}
